SEARCH_QUERY = """
query LodgingPwaPropertySearch($context: ContextInput!, $destination: DestinationInput!, $rooms: [RoomInput!], $dateRange: PropertyDateRangeInput, $sort: PropertySort, $filters: PropertySearchFiltersInput, $marketing: PropertyMarketingInfoInput, $legacyCriteria: LegacyPropertySearchCriteriaInput, $propertyShopOptions: PropertyShopOptionsInput, $searchPagination: PaginationInput, $searchIntent: SearchIntentInput, $shoppingContext: ShoppingContextInput, $criteria: PropertySearchCriteriaInput, $shouldFetchSortAndFilter: Boolean = true) {
  propertySearch(context: $context, destination: $destination, rooms: $rooms, dateRange: $dateRange, sort: $sort, filters: $filters, marketing: $marketing, legacyCriteria: $legacyCriteria, propertyShopOptions: $propertyShopOptions, searchPagination: $searchPagination, searchIntent: $searchIntent, shoppingContext: $shoppingContext, criteria: $criteria) {
    searchCriteria {
      propertyShopOptions {
        points
      }
      dateRange {
        checkInDate {
          ...CommonDateFields
        }
        checkOutDate {
          ...CommonDateFields
        }
      }
      destination {
        regionId
        regionName
      }
      searchIntent {
        theme
        userIntent
        semdtl
      }
      sort
      filters {
        accessibility
        amenities
        bedroomFilter
        commissionTiers
        agencyBusinessModels
        deals
        paymentType
        poi
        priceBuckets
        propertyName
        propertyStyles
        reviewScore {
          min
          max
        }
        starList
        structureTypes
        travelerType
        mealPlan
        cleaningAndSafetyPractices
      }
    }
    sortAndFilter @include(if: $shouldFetchSortAndFilter) {
      defaults {
        sort
        regionId
      }
      selected {
        priceFilterPills {
          aggregate {
            label
            value
          }
          buckets
        }
        star
      }
      options {
        accessibilityLabel
        appliedFilterCount
        sortAndFilter {
          selected
          isRange
          label
          max
          min
          placeholder
          step
          subLabel
          name
          title
          hiddenThreshold: seeMoreOptionsToggleThreshold
          options {
            selectedLabel
            ariaLabel
            description
            icon
            isSelected
            label
            value
            optionValue
            range {
              min
              max
            }
            filterType
          }
        }
      }
    }
    propertySearchListings {
      __typename
      ... on Property {
        ...PropertyFields
      }
      ... on MessageResult {
        ...MessageFields
      }
      ... on LodgingHeading {
        value
        size
        tag
      }
      ... on StaticLodgingMultiItemCrossSell {
        crossSellProductType
        fallbackListing {
          __typename
          ... on MessageResult {
            ...MessageFields
          }
        }
      }
    }
    summary {
      resultsSummary {
        __typename
        value
        ... on LodgingLinkMessage {
          ...SearchLinkMessage
        }
        ... on LodgingDialogTriggerMessage {
          ...SearchDialogMessage
        }
      }
      pricedHotelSize
      region {
        name
        id
      }
      resultSectionHeadings {
        heading
        index
      }
      loyaltyEducation {
        action {
          href
          rfrr
          text
        }
        content {
          __typename
          ...PointsEducationFragment
          ...ProgramEducationFragment
        }
        title
      }
      loyaltyInfo {
        pointsAppliedMessage
        saveWithPointsMessage
        saveWithPointsActionMessage
      }
      matchedPropertiesSize
      resultsHeading
    }
    navigationTabs {
      tabs {
        localizedName
        sectionName
        state
        tabLink {
          link {
            url
            uri {
              value
            }
            target
          }
          value
        }
      }
    }
    map {
      bounds {
        northeast {
          latitude
          longitude
        }
        southwest {
          latitude
          longitude
        }
      }
      center {
        latitude
        longitude
      }
      markers {
        mapMarker {
          label
          icon
          type
          latLong {
            latitude
            longitude
          }
          clientSideAnalytics {
            referrerId
            linkName
          }
        }
        __typename
        ... on Property {
          ...CommonPropertyCardFields
        }
        ... on PointOfInterest {
          name: title
        }
      }
      staticMapSrc
      title
      subtitle
      zoom
      messagingModel {
        title {
          text
          theme
          icon {
            description
            id
          }
        }
        subtitle {
          text
          theme
          icon {
            description
            id
          }
        }
        type
      }
    }
    exitIntent {
      logoUrl
      backgroundImageUrl
      clickHereLinkUrl
      message {
        headingOne
        headingTwo
        headingThree
        couponCode
        percentOff
        termsAndConditionsOne
        termsAndConditionsTwo
        clickHere
      }
    }
    legalDisclaimer {
      content {
        markupType
        text
      }
    }
    shoppingContext {
      multiItem {
        id
        packageType
      }
    }
    multiItemSearchContext {
      ...MultiItemPropertySearchContextFields
      cars {
        primary {
          pickUpDateTime {
            ...CommonDateTimeFields
          }
          dropOffDateTime {
            ...CommonDateTimeFields
          }
          pickUpLocation {
            airportCode
          }
          dropOffLocation {
            airportCode
          }
        }
      }
      flights {
        primary {
          travelers {
            type
            age
          }
          tripType
          journeyCriterias {
            destination
            origin
            departureDate {
              day
              month
              year
            }
          }
          searchPreferences {
            airline
            advancedFilters
            cabinClass
          }
        }
      }
    }
    errorResponse {
      header
      body
      icon {
        description
        id
      }
      button {
        primary
        action {
          ... on UILinkAction {
            analytics {
              referrerId
              linkName
            }
            resource {
              ... on HttpURI {
                relativePath
                value
              }
            }
          }
        }
        disabled
      }
      errorRecoveryButtons {
        primary
        action {
          ... on UILinkAction {
            analytics {
              referrerId
              linkName
            }
            resource {
              ... on HttpURI {
                relativePath
                value
              }
            }
          }
        }
        disabled
      }
    }
  }
}

fragment MultiItemPropertySearchContextFields on MultiItemSearchContext {
  properties {
    primary {
      rooms {
        adults
      }
      destination {
        regionId
        regionName
      }
      dateRange {
        checkInDate {
          ...CommonDateFields
        }
        checkOutDate {
          ...CommonDateFields
        }
      }
    }
  }
}

fragment MessageFields on MessageResult {
  title {
    ...MessageTitleFields
  }
  subtitle {
    ...MessageTitleFields
  }
  action {
    primary {
      ...MessagingActionFields
    }
    secondary {
      ...MessagingActionFields
    }
  }
  index
  type
}

fragment MessageTitleFields on MessagingResultTitle {
  text
  icon {
    description
    id
  }
  mark {
    description
    id
  }
  illustration {
    assetUri {
      value
    }
    description
  }
  theme
}

fragment MessagingActionFields on MessagingAction {
  actionDetails {
    details
    name
    title
    accessibilityLabel
  }
  linkUrl
  referrerId
  text
}

fragment PropertyFields on Property {
  ...CommonPropertyCardFields
  star
  starRatingIcon
  availability {
    available
    text
    theme
  }
  offerSummary {
    messages {
      message
      theme
      type
      mark {
        id
      }
    }
  }
  legalDisclaimer {
    title
    disclaimerContents
  }
  imageGallery {
    accessibilityLabel
    images {
      image {
        url
        description
      }
      subjectId
      fallbackImage {
        url
        description
      }
      imageId
    }
  }
  mapMarker {
    icon
    label
    type
    latLong {
      latitude
      longitude
    }
    clientSideAnalytics {
      referrerId
      linkName
    }
  }
  neighborhood {
    name
  }
  offerBadge {
    primary {
      text
      theme_temp
      icon_temp {
        id
        description
      }
      mark {
        id
        description
      }
    }
    secondary {
      text
      theme_temp
      icon_temp {
        id
        description
      }
    }
  }
  pinnedDetails {
    heading
  }
  recentlyViewed {
    id
    description
  }
  featuredMessages {
    ...featuredMessage
  }
  supportingMessages
  shortList {
    favorited
    saveUrl
    removeUrl
    metaData {
      chkIn
      chkOut
      hotelId
      roomConfiguration
    }
  }
  highlightedPropertyDetails
  propertySource {
    accessibilityLabel
    label
    graphic {
      __typename
      ... on Mark {
        description
        id
        size
        token
        url {
          value
        }
      }
    }
    text {
      value
    }
  }
  dataAttributes {
    key
    value
  }
  listingFooter {
    actionDetails {
      name
    }
    icon {
      description
      id
    }
    linkUrl
    referrerId
    text
  }
}

fragment SearchLinkMessage on LodgingLinkMessage {
  label
  link {
    ...SearchLink
  }
  icon {
    id
  }
}

fragment SearchDialogMessage on LodgingDialogTriggerMessage {
  dialogTrigger {
    dialogName
    referrerId
    actionDetails {
      linkUrl
      referrerId
      message
      text
    }
  }
  icon {
    id
  }
}

fragment SearchLink on LodgingLink {
  url
  referrerId
}

fragment DisplayPriceFragment on DisplayPrice {
  __typename
  role
  price {
    formatted
    accessibilityLabel
  }
  disclaimer {
    content
    primaryUIButton {
      accessibility
      primary
    }
  }
}

fragment EnrichedMessageFragment on LodgingEnrichedMessage {
  __typename
  value
  state
}

fragment CommonPropertyCardFields on Property {
  id
  name
  propertyImage {
    image {
      description
      url
    }
    fallbackImage {
      description
      url
    }
  }
  offerBadge {
    primary {
      text
      theme_temp
      icon_temp {
        id
        description
      }
      mark {
        id
        description
      }
    }
    secondary {
      text
      theme_temp
      icon_temp {
        id
        description
      }
    }
  }
  price {
    alignment
    displayMessages {
      lineItems {
        ...DisplayPriceFragment
        ...EnrichedMessageFragment
      }
    }
    lead {
      formatted
    }
    strikeOutType
    strikeOut {
      formatted
    }
    disclaimer {
      value
    }
    roomNightMessage
    priceMessages {
      value
    }
    marketingFeeDetails {
      tierName
      tierIcon
      marketingFeeMessage {
        value
      }
    }
    options {
      leadingCaption
      displayPrice {
        formatted
      }
      strikeOut {
        formatted
      }
      loyaltyPrice {
        amount {
          formatted
        }
        totalStrikeOutPoints {
          formatted
        }
        unit
      }
      disclaimer {
        value
      }
    }
  }
  reviews {
    score
    localizedScore
    total
    localizedTotal
    superlative
    localizedSubtitle
    localizedSubtitleA11y {
      accessibilityLabel
      value
    }
    mark {
      id
      description
    }
  }
  destinationInfo {
    distanceFromMessaging
  }
  vipMessaging
  propertyDetailsLink {
    uri {
      value
      relativePath
    }
    clientSideAnalytics {
      referrerId
      linkName
    }
  }
  sponsoredListing {
    id
    clickRedirectTrackingUrl
    clickTrackingUrl
    details
    detailsHeadline
    hotelImage
    impressionTrackingUrl
    trackingData
    brand
    clickRedirectLinkoffTrackingUrl
    logo
    lotagline
    rating
    slots
    vanityUrl
    rank
    position
  }
}

fragment CommonDateFields on Date {
  year
  month
  day
}

fragment CommonDateTimeFields on DateTime {
  year
  month
  day
  hour
  minute
  second
}

fragment PointsEducationFragment on LoyaltyPointsEducation {
  description
  programFeatures {
    description
    perks {
      ...PerksFragment
    }
    title
  }
  heroImage {
    url
    description
  }
}

fragment ProgramEducationFragment on LoyaltyProgramEducation {
  joinProgramText
  perks {
    ...PerksFragment
  }
}

fragment PerksFragment on LoyaltyEducationPerks {
  descriptions
  icon
}

fragment featuredMessage on LodgingEnrichedMessage {
  icon {
    id
    description
    size
  }
  value
}
"""

