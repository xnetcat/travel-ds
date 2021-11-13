SEARCH_QUERY = """
fragment FilterRangeFragment on FilterRange {
  min {
    value
    defaultValue
    __typename
  }
  max {
    value
    defaultValue
    __typename
  }
  increments
  __typename
}

fragment FilterWithItemsFragment on FilterWithItems {
  label
  applied
  items {
    label
    value
    applied
    disabled
    mappedIds
    requestParameterName
    filterCategory
    minValue
    maxValue
    __typename
  }
  __typename
}

query searchPageQuery($sqmState: SqmState!, $filterState: FilterState, $pagination: SearchPaginationState, $pageName: String, $points: Boolean) {
  searchPage(sqmState: $sqmState, pagination: $pagination, filterState: $filterState, points: $points) {
    id
    page {
      ...PageFragment
      __typename
    }
    header {
      ...HeaderFragment
      __typename
    }
    chassis {
      ...ChassisFragment
      __typename
    }
    body {
      ... on SrpBodyError {
        error {
          message
          __typename
        }
        __typename
      }
      ... on SrpBodySuccess {
        searchResults {
          totalCount
          narrowResultsText
          travelAdsAvailableOnSortedSearch
          pagination {
            currentPage
            nextPageUrl
            __typename
          }
          algoGeoBulletsTracking
          results {
            ...SearchHotelResultFragment
            __typename
          }
          unavailableCount
          brandMultiPropertyCarouselResult {
            ...BrandMultiPropertyCarouselResultFragment
            __typename
          }
          __typename
        }
        sortResults {
          defaultSortApplied
          distanceOptionLandmarkId
          sortLandmarkId
          options {
            label
            selectedChoiceLabel
            choices {
              label
              value
              href
              selected
              __typename
            }
            enhancedChoices {
              label
              choices {
                label
                id
                __typename
              }
              __typename
            }
            __typename
          }
          __typename
        }
        filters {
          applied
          name {
            disabled
            item {
              hotelId
              value
              __typename
            }
            __typename
          }
          popular {
            ...FilterWithItemsFragment
            __typename
          }
          price {
            disabled
            label
            range {
              ...FilterRangeFragment
              __typename
            }
            multiplier
            __typename
          }
          guestRating {
            disabled
            applied
            range {
              ...FilterRangeFragment
              __typename
            }
            __typename
          }
          starRating {
            label
            applied
            items {
              label
              value
              applied
              disabled
              mappedIds
              requestParameterName
              filterCategory
              minValue
              maxValue
              __typename
            }
            __typename
          }
          paymentPreference {
            ...FilterWithItemsFragment
            __typename
          }
          welcomeRewards {
            ...FilterWithItemsFragment
            __typename
          }
          neighbourhood {
            ...FilterWithItemsFragment
            __typename
          }
          landmarks {
            ...FilterWithItemsFragment
            __typename
          }
          accommodationType {
            ...FilterWithItemsFragment
            __typename
          }
          facilities {
            ...FilterWithItemsFragment
            __typename
          }
          themesAndTypes {
            ...FilterWithItemsFragment
            __typename
          }
          accessibility {
            ...FilterWithItemsFragment
            __typename
          }
          __typename
        }
        pointOfSale {
          currency {
            separators
            format
            __typename
          }
          __typename
        }
        loyalty {
          ...LoyaltyFragment
          __typename
        }
        miscellaneous {
          disclaimer
          fullSccFormat
          pageViewBeaconUrl
          showSortDisclaimer
          interactiveSortDisclaimer
          sortDisclaimer
          compressionMessaging {
            percentage
            popularityMessage
            __typename
          }
          rewardBanner {
            autoOpen
            type
            punchCard {
              collectedNights
              reservedNights
              freeNights
              closeToEarn
              punchCardMessage
              __typename
            }
            __typename
          }
          isAutoPopulatedDate
          ads {
            es5LibraryUrl
            adsLoaderUrl
            adsPositions
            nativeBrandListingPosition
            pageId
            targetingConfig {
              mc1
              CMPTST
              d
              ssl
              kid
              dta
              ets
              ete
              pd
              __typename
            }
            __typename
          }
          showMetaOccupancyNotification
          travelAdvisoryBannerMessaging {
            title
            message
            links {
              text
              url
              __typename
            }
            __typename
          }
          freeCancellationBannerMessaging {
            head
            description
            __typename
          }
          noCreditCardFilterReportable
          payPalFilterReportable
          kesAppDownloadMessaging {
            ...AppDownloadMessagingFragment
            __typename
          }
          __typename
        }
        packageRates {
          message
          packageRateIcon
          __typename
        }
        alternativeDestinationsModule {
          ...AlternativeDestinationFragment
          __typename
        }
        __typename
      }
      __typename
    }
    footer {
      ...FooterFragment
      redemptionFee {
        link {
          label
          href
          rel
          target
          __typename
        }
        message
        __typename
      }
      __typename
    }
    __typename
  }
}

fragment PageFragment on Page {
  head {
    linkedData
    __typename
  }
  __typename
}

fragment NavigationLinkFragment on NavigationLink {
  label
  linkId
  url
  icon
  rel
  class
  number
  children {
    kes_icon
    label
    linkId
    class
    url
    icon
    rel
    number
    __typename
  }
  __typename
}

fragment HeaderFragment on Header {
  id
  tracking {
    consentGiven
    callCcaOnInit
    showBanner
    __typename
  }
  pos {
    label
    __typename
  }
  navigationLinks {
    top {
      ...NavigationLinkFragment
      __typename
    }
    topAlt {
      ...NavigationLinkFragment
      __typename
    }
    bottom {
      ...NavigationLinkFragment
      __typename
    }
    bottomAlt {
      ...NavigationLinkFragment
      __typename
    }
    __typename
  }
  userPrivacyPreferences {
    dnsmpi
    __typename
  }
  user {
    is_identified
    is_logged_in
    hcom_rewards_tier
    channel
    __typename
  }
  newsletterSignUpAnywhere {
    nativeApplicationDownloadUrl
    privacyPolicyLink
    termsAndConditionsLink
    proxyUrl
    targetOrigin
    __typename
  }
  context {
    includeCurrencyOption
    flagIso
    currencyLabel
    __typename
  }
  cobrand
  headerConfig {
    logoPosition
    orderFlipped
    sameColors
    mobileMenuPosition
    __typename
  }
  poweredBy
  __typename
}

fragment ChassisFragment on Chassis {
  id
  page {
    pageTitle
    metas
    links
    cdb
    mdl
    omniture
    __typename
  }
  user {
    firstName
    consent {
      callCcaOnInit
      consentGiven
      showBanner
      dnsmpi
      __typename
    }
    favourites
    __typename
  }
  tracking {
    harvesterUrl
    travelPixelEnv
    tagCommanderUrl
    googleTagManagerId
    omnitureAccount
    __typename
  }
  mainImage {
    href
    focus
    enabled
    __typename
  }
  appContext {
    pos
    channel
    platform
    currency
    locale
    brandId
    langdir
    isKnownUser
    clientId
    clientVersion
    authenticationState
    guid
    customerId
    subscriber
    __typename
  }
  srs {
    suggest
    resolve
    recommend
    commonParams {
      providerInfoTypes
      locale
      __typename
    }
    __typename
  }
  sqm {
    destination {
      id
      value
      type
      resolvedLocation {
        name
        latitude
        longitude
        __typename
      }
      shortName
      latitude
      longitude
      __typename
    }
    toSRPdestination {
      id
      value
      type
      __typename
    }
    title
    checkIn
    checkOut
    rooms
    firstDayOfWeek
    adults
    kids
    isVisible
    __typename
  }
  filter {
    accessibility
    accommodationType
    amenities
    applied
    brands
    facilities
    guestRating {
      min
      max
      __typename
    }
    landmarks
    name {
      id
      value
      __typename
    }
    neighbourhood
    paymentPreference
    popular
    price {
      min
      max
      multiplier
      defaultMax
      __typename
    }
    sortLandmarkId
    sortOrder
    starRating
    themesAndTypes
    types
    vrFilterClicked
    welcomeRewards
    __typename
  }
  navigation {
    pathname
    rateplanId
    search
    sbgState {
      rooms
      kids
      adults
      __typename
    }
    points
    __typename
  }
  __typename
}

fragment FooterFragment on Footer {
  id(id: $pageName)
  links {
    label
    href
    children {
      label
      href
      rel
      target
      item_meta {
        id
        class
        __typename
      }
      __typename
    }
    rel
    target
    sub_label
    item_meta {
      id
      class
      __typename
    }
    __typename
  }
  copyright
  loyaltyProgramLink {
    label
    href
    rel
    target
    __typename
  }
  trustMessage
  legallyCompliantPricesMessage
  __typename
}

fragment SearchHotelResultFragment on SearchResult {
  hotelId
  imageId
  hostType
  addNoFollow
  searchHotelDetails {
    ...SearchHotelDetailsFragment
    __typename
  }
  pinned {
    info
    reason
    isStopSell
    reasonCode
    __typename
  }
  sponsored {
    impressionTrackingUrl
    clickTrackingUrl
    travelAdDetails
    travelAdDetailsHeadLine
    travelAdHotelImage
    __typename
  }
  coupon
  deal {
    ...DealFragment
    __typename
  }
  neighbourhood
  geoBullets
  propertyType
  popularAmenities {
    type
    description
    __typename
  }
  altText
  ratePlan {
    price {
      ...SearchResultRatePlanPriceFragment
      __typename
    }
    features {
      instalmentsMessage
      noCCRequired
      freeCancellation
      payAtPropertyBadge
      __typename
    }
    __typename
  }
  coordinate {
    lat
    lon
    __typename
  }
  roomsLeft
  soldOut
  dealOfTheDay
  isInExpandedArea
  badging {
    hotelBadge {
      type
      label
      loyaltyTier
      tooltipTitle
      tooltipText
      percentile
      __typename
    }
    secretPriceBadge
    __typename
  }
  couponBadge {
    badgeName
    tooltip
    badgeText
    linkText
    linkPath
    __typename
  }
  vip
  urls {
    alternativeOccupancy {
      adults
      kids
      __typename
    }
    __typename
  }
  rlsa
  isGreatMatch
  imageTrackingInfo
  hotelMessage
  vitality
  bedTypeOccupancy
  isVrboProperty
  __typename
}

fragment SearchHotelDetailsFragment on SearchHotelDetails {
  id
  name
  vrBadge
  optimizedThumbUrl
  optimizedCompactThumbUrl
  optimizedImages {
    imageUrl
    title
    __typename
  }
  address {
    countryName
    locality
    postalCode
    region
    streetAddress
    obfuscate
    __typename
  }
  fullAddress
  locationCoordinates {
    latitude
    longitude
    __typename
  }
  starRating
  guestReviews {
    rating
    lowRating
    badgeText
    total
    __typename
  }
  welcomeRewards {
    tooltipText
    collect
    redeem
    __typename
  }
  selectButtonText
  __typename
}

fragment SearchResultRatePlanPriceFragment on SearchResultRatePlanPrice {
  current
  secondaryFormatted
  exactCurrent
  old
  info
  summary
  fromPrice
  supplierCollectedCharges
  totalPricePerStay
  fullyBundledPricePerStay
  roomCount
  priceBreakdown {
    title
    callToActionLabel
    includedMeals {
      label
      type
      __typename
    }
    lineItems {
      label
      feeDetails
      price
      __typename
    }
    total {
      label
      price
      __typename
    }
    additionalFees {
      label
      price
      __typename
    }
    totalIncludingAdditionalFees {
      label
      price
      __typename
    }
    ecaMessage
    __typename
  }
  __typename
}

fragment DealFragment on Deal {
  text
  type
  purpose
  discountPercent
  translation
  packageRateIcon
  __typename
}

fragment BrandMultiPropertyCarouselResultFragment on BrandMultiPropertyCarouselResult {
  brandAdCopy
  brandLogo
  position
  title
  seeAllPropertiesURLText
  brandIds
  properties {
    ...SearchHotelResultFragment
    __typename
  }
  __typename
}

fragment AlternativeDestinationFragment on AlternativeDestinationList {
  category
  key
  title
  egRecsResponseData {
    responseId
    success
    __typename
  }
  cards {
    gaiaId
    destinationId
    propertyTypeName
    image {
      src
      alt
      author {
        name
        url
        origin
        license {
          suite
          url
          __typename
        }
        __typename
      }
      __typename
    }
    title
    description
    popUpSqmTitle
    filters {
      accommodationType
      amenities
      starRating
      types
      themesAndTypes
      __typename
    }
    link
    __typename
  }
  __typename
}

fragment AppDownloadMessagingFragment on KesAppDownloadMessagingModular {
  downloadAppUrl
  enabled
  id
  category
  key
  heading
  body
  __typename
}

fragment LoyaltyFragment on Loyalty {
  pointsToggle {
    pointsName
    enabled
    infoMessage
    airMilesChecked
    __typename
  }
  banner {
    message
    sidebarMessage
    __typename
  }
  __typename
}
"""
