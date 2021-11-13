LISTING_QUERY = """
query propertyPageQuery($sqmState: SqmState!, $filterState: FilterState, $sbgState: SbgStateScalar, $rateplanId: String, $pageName: String, $points: Boolean) {
  propertyPage(sqmState: $sqmState, filterState: $filterState, rateplanId: $rateplanId, sbgState: $sbgState, points: $points) {
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
      breadcrumb {
        ...BreadcrumbFragment
        __typename
      }
      pageType
      pdpHeader {
        backToSRPLink
        backToSRPText
        destinationId
        hotelLocation {
          coordinates {
            latitude
            longitude
            __typename
          }
          resolvedLocation
          locationName
          __typename
        }
        hotelId
        __typename
      }
      propertyDescription {
        name
        address {
          countryName
          locality
          postalCode
          region
          streetAddress
          obfuscate
          __typename
        }
        images {
          numberOfPropertyImages
          propertyImages {
            imageId
            title
            extendedCaptionOverlay
            imageUrl
            categoryGroup
            thumbImageUrl
            trackingDetails
            __typename
          }
          optimizedThumbUrl
          optimizedCompactThumbUrl
          __typename
        }
        starRatingTitle
        starRating
        mapWidget {
          smallTouchBackground
          __typename
        }
        tagline
        hostType
        freebies
        clientToken
        vrBadge
        renovationInfo
        singleUnitVacationRental
        propertyOverviewList {
          type
          info
          applied
          __typename
        }
        propertyOverviewTitle
        renovationInfoBanner {
          propertyBanner
          facilitiesBanner
          __typename
        }
        supplierType
        roomTypeNames
        freeCancellation
        vitality
        __typename
      }
      welcomeRewards {
        applies
        collectText
        toolTip
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
      guestReviews {
        brands {
          rating
          lowRating
          badgeText
          total
          seoReviews {
            ...GuestReviewsFragment
            __typename
          }
          featuredReviews {
            text
            footerText
            __typename
          }
          __typename
        }
        urls {
          standalone
          __typename
        }
        __typename
      }
      featuredPrice {
        pricingTooltip
        oldPrice
        currentPrice {
          formatted
          plain
          __typename
        }
        secondaryPrice {
          message
          __typename
        }
        fromPrice
        priceInfo
        priceSummary
        deal {
          ...DealFragment
          __typename
        }
        mandatoryFee
        fullyBundledPricePerStay
        totalPricePerStay
        roomsLeft
        roomCount
        instalmentsMessage
        memberOnlyDealAvailable
        moduleDisabled
        datelessFeaturedPriceAvailability {
          message
          tooltipMessage
          __typename
        }
        __typename
      }
      overview {
        overviewSections {
          id
          title
          type
          content
          contentType
          extraContent
          __typename
        }
        popularAmenities {
          type
          info
          applied
          __typename
        }
        propertyLocationReviews {
          mainHeader
          mainTooltip
          totalNumberOfReviews
          reviewGroups {
            tagName
            positiveReviewCount
            tagTooltip
            tagSubHeader
            __typename
          }
          __typename
        }
        sleepingArrangements {
          maximumOccupancy {
            messageTotal
            messageChildren
            __typename
          }
          bedTypesPerRoom {
            name
            bedGroups {
              label
              beds
              __typename
            }
            __typename
          }
          __typename
        }
        __typename
      }
      alternativeDates {
        currentPrice
        stayPeriod
        offset
        pdpUrl
        cheapest
        __typename
      }
      datelessFlowAlternativeDates {
        title
        items {
          currentPrice
          stayPeriod
          date
          label
          stayNights
          url
          cheapest
          __typename
        }
        __typename
      }
      travelAdvisoryBannerMessaging {
        text
        link {
          text
          url
          __typename
        }
        __typename
      }
      propertyRestrictions {
        list
        summary {
          text
          link {
            text
            url
            __typename
          }
          __typename
        }
        __typename
      }
      atAGlance {
        keyFacts {
          hotelSize
          propertySizeLabel
          arrivingLeaving
          specialCheckInInstructions
          requiredAtCheckIn
          __typename
        }
        travellingOrInternet {
          travelling {
            children
            pets
            __typename
          }
          internet
          __typename
        }
        transportAndOther {
          transport {
            transfers
            parking
            __typename
          }
          acceptedPaymentMethods {
            text
            option
            __typename
          }
          otherInformation
          __typename
        }
        __typename
      }
      amenities {
        heading
        type
        listItems {
          heading
          containsHTML
          listItems
          __typename
        }
        __typename
      }
      smallPrintSection {
        alternativeNames
        hotelRegistryNumber
        hostType
        hideHostType
        optionalExtras
        policies
        mandatoryTaxesOrFees
        display
        mandatoryFees
        __typename
      }
      whatsAround {
        landmarks
        transport
        locationDescriptionCallbackUrl
        __typename
      }
      whatsAroundPdpProfile {
        imageUrl
        description
        title
        __typename
      }
      loyalty {
        ...LoyaltyFragment
        __typename
      }
      hygieneAndCleanliness {
        title
        hygieneQualifications {
          title
          qualifications
          __typename
        }
        healthAndSafetyMeasures {
          title
          description
          measures
          __typename
        }
        __typename
      }
      vrPropertyDescription {
        title
        text
        showInMoreInfoSection
        __typename
      }
      specialFeatures {
        sections {
          heading
          freeText
          __typename
        }
        __typename
      }
      vip
      hotelBadge {
        type
        label
        loyaltyTier
        tooltipTitle
        tooltipText
        __typename
      }
      roomsAndRates {
        ...RoomsAndRatesFragment
        __typename
      }
      apartment {
        sectionTitle
        amenities {
          header
          list
          __typename
        }
        __typename
      }
      manager {
        title
        name
        languages
        profileImage
        hostType
        hideHostType
        __typename
      }
      houseRules {
        sections {
          section
          list
          paragraph
          __typename
        }
        __typename
      }
      feesAndPolicies {
        sections {
          section
          header
          paragraph
          list
          __typename
        }
        registrationNumber
        hostType
        hideHostType
        __typename
      }
      seoSchema {
        schema
        __typename
      }
      unavailable {
        isStopSell
        __typename
      }
      miscellaneous {
        pageViewBeaconUrl
        priceMatchGuaranteeUrl
        hotelRegistryNumber
        checkInRatingUrl
        hasSearchFiltersApplied
        childStaysFreeBadge {
          label
          tooltipText
          __typename
        }
        __typename
      }
      query {
        alternativeOccupancy {
          adults
          kids
          __typename
        }
        __typename
      }
      moreInfoSections {
        id
        title
        wideLayout
        sections {
          title
          content
          hideContent
          alternativeContent
          acceptedPaymentMethods {
            text
            option
            __typename
          }
          contentType
          __typename
        }
        sectionsVariant {
          title
          content
          hideContent
          alternativeContent
          contentType
          __typename
        }
        initialState
        __typename
      }
      perfectPropertyModule {
        destinationName
        backToSearchUrl
        __typename
      }
      locationLandmarks
      familyFriendly
      ads {
        es5LibraryUrl
        adsLoaderUrl
        hideAdsBasedOnRoomAndRates
        pageId
        targetingConfig {
          mc1
          CMPTST
          activity
          d
          ssl
          kid
          dta
          ets
          ete
          sr
          pd
          __typename
        }
        __typename
      }
      goldContentDescription
      frequentlyAskedQuestionsSection {
        data {
          question
          answer
          type
          __typename
        }
        questionThemes
        schema
        __typename
      }
      kesAppDownloadMessaging {
        ...AppDownloadMessagingFragment
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

fragment BreadcrumbFragment on Breadcrumb {
  href
  label
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

fragment DealFragment on Deal {
  text
  type
  purpose
  discountPercent
  translation
  packageRateIcon
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

fragment GuestReviewsFragment on ReviewsItem {
  genuineMsg
  tripType
  tripTypeText
  reviewDate
  reviewSubmitDate
  rating
  reviewer {
    name
    locality
    locale
    __typename
  }
  badge
  summary
  description
  __typename
}

fragment RoomPriceFragment on RoomRatePlanPrice {
  current
  totalPriceInUSD
  secondaryFormatted
  old
  info
  loyaltySummary
  summaryType
  mandatoryFee
  resortFeeExclusionText
  bookingWithPointsDisabled
  fullyBundledPricePerStay
  totalPricePerStay
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

fragment RoomPaymentFragment on RoomRatePlanPayment {
  book {
    caption
    bookingFormParams {
      key
      value
      __typename
    }
    bookingParams {
      rateCode
      __typename
    }
    bookingParamsMixedRatePlan {
      orderItems {
        rateCode
        __typename
      }
      __typename
    }
    isMixedRatePlan
    __typename
  }
  options {
    type
    headerText
    ctaText
    updatedReserveWithDepositTitle
    displayedPrice {
      displayedPrice
      secondaryFormatted
      priceInfo
      roomCount
      approximated
      fullyBundledPricePerStay
      totalPricePerStay
      priceSummary
      __typename
    }
    conditions {
      type
      message
      __typename
    }
    welcomeRewards {
      collect
      redeem
      __typename
    }
    bookingParams {
      key
      value
      __typename
    }
    __typename
  }
  noCCRequired
  paymentMessage
  __typename
}

fragment RoomOfferFragment on RoomRatePlanOffers {
  offer {
    text
    promoType
    __typename
  }
  valueAdds {
    id
    info
    additionalInfo
    __typename
  }
  artificiallyFencedRatesOffer {
    hotelChainId
    info
    additionalInfo
    __typename
  }
  vipBenefits {
    header
    tooltipTitle
    tooltipText
    eligibilityLoyaltyTier
    valueAddedPromotions {
      description
      category
      __typename
    }
    __typename
  }
  vitality
  __typename
}

fragment RoomsFragment on Room {
  name
  roomId
  images {
    imageId
    caption
    thumbnailUrl
    fullSizeUrl
    trackingDetails
    __typename
  }
  maxOccupancy {
    messageTotal
    messageChildren
    __typename
  }
  bedTypeAndOccupancy {
    bedTypes
    extraBeds
    __typename
  }
  additionalInfo {
    description
    details {
      amenities
      exposedAmenities {
        roomSize
        __typename
      }
      __typename
    }
    viewBadge
    viewBadgeAvailable
    __typename
  }
  moreChoicesToggle {
    title
    description
    __typename
  }
  ratePlans {
    asSeenOn
    isGreatMatchOption
    ratePlanComparedToCheapest {
      listOfDifferences
      moreDifferences
      __typename
    }
    cancellations {
      title
      free
      info
      additionalInfo
      period
      refundable
      __typename
    }
    featureList {
      type
      title
      info
      alternativeInfo
      reviewInfo {
        text
        score
        __typename
      }
      additionalInfo
      premium
      dataSourceInfo
      __typename
    }
    features {
      featureType
      title
      info
      alternativeInfo
      reviewInfo {
        text
        score
        __typename
      }
      dataSourceInfo
      __typename
    }
    payAtPropertyBadge {
      title
      info
      __typename
    }
    welcomeRewards {
      tooltipText
      collect
      redeem
      __typename
    }
    instalmentsMessage
    offers {
      ...RoomOfferFragment
      __typename
    }
    roomsLeft
    price {
      ...RoomPriceFragment
      __typename
    }
    payment {
      ...RoomPaymentFragment
      __typename
    }
    highlighted
    nonPricePromotions {
      options {
        category
        description
        __typename
      }
      __typename
    }
    deal {
      ...DealFragment
      __typename
    }
    pointsMessage
    __typename
  }
  largestRoomBadge
  isMultisourceRoom
  __typename
}

fragment RoomsAndRatesFragment on RoomsAndRates {
  commonSettings {
    columnHeadings {
      priceColumnHeading
      loyaltyHeading
      __typename
    }
    label
    loyaltyTier
    bookingUrl
    refundableDepositMessage
    refundableDepositTooltip
    nudgeMessaging {
      title
      description
      __typename
    }
    freeCancellationAndNonRefundableRateplansExist
    __typename
  }
  groups {
    base {
      headerText
      numberOfRatesShownPerRoom
      rooms {
        ...RoomsFragment
        __typename
      }
      cheapestRooms {
        rooms {
          roomId
          ratePlanId
          ratePlanLocation
          __typename
        }
        priceInUSD
        __typename
      }
      __typename
    }
    recommended {
      headerText
      numberOfRatesShownPerRoom
      rooms {
        ...RoomsFragment
        __typename
      }
      __typename
    }
    recommendedOffer {
      headerText
      rooms {
        numberOfRoomType
        guestNumber
        ...RoomsFragment
        __typename
      }
      sectionPrice {
        priceHeading
        price {
          ...RoomPriceFragment
          __typename
        }
        payment {
          ...RoomPaymentFragment
          __typename
        }
        offers {
          ...RoomOfferFragment
          __typename
        }
        deal {
          ...DealFragment
          __typename
        }
        __typename
      }
      __typename
    }
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